"""Local python-for-android recipe for pygame-ce on SDL2."""

from os.path import join

from pythonforandroid.recipe import CompiledComponentsPythonRecipe
from pythonforandroid.toolchain import current_directory


class PygameCeRecipe(CompiledComponentsPythonRecipe):
    version = "2.5.0"
    url = "https://github.com/pygame-community/pygame-ce/archive/refs/tags/{version}.tar.gz"
    name = "pygame-ce"
    site_packages_name = "pygame-ce"

    depends = [
        "sdl2",
        "sdl2_image",
        "sdl2_mixer",
        "sdl2_ttf",
        "setuptools",
        "jpeg",
        "png",
    ]

    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            template = open(join("buildconfig", "Setup.Android.SDL2.in"), encoding="utf-8").read()
            env = self.get_recipe_env(arch)
            env["ANDROID_ROOT"] = join(self.ctx.ndk.sysroot, "usr")

            png_recipe = self.get_recipe("png", self.ctx)
            png_lib = join(png_recipe.get_build_dir(arch.arch), ".libs")
            png_inc = png_recipe.get_build_dir(arch)

            jpeg_recipe = self.get_recipe("jpeg", self.ctx)
            jpeg_root = jpeg_recipe.get_build_dir(arch.arch)

            mixer = self.get_recipe("sdl2_mixer", self.ctx)
            mixer_inc = " ".join("-I" + path for path in mixer.get_include_dirs(arch))

            setup = template.format(
                sdl_includes=(
                    " -I" + join(self.ctx.bootstrap.build_dir, "jni", "SDL", "include")
                    + " -L" + join(self.ctx.bootstrap.build_dir, "libs", str(arch))
                    + " -L" + png_lib
                    + " -L" + jpeg_root
                    + " -L" + arch.ndk_lib_dir_versioned
                ),
                sdl_ttf_includes="-I" + join(self.ctx.bootstrap.build_dir, "jni", "SDL2_ttf"),
                sdl_image_includes="-I" + join(self.ctx.bootstrap.build_dir, "jni", "SDL2_image"),
                sdl_mixer_includes=mixer_inc,
                jpeg_includes="-I" + jpeg_root,
                png_includes="-I" + png_inc,
                freetype_includes="",
            )
            open("Setup", "w", encoding="utf-8").write(setup)

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env["USE_SDL2"] = "1"
        env["PYGAME_CROSS_COMPILE"] = "TRUE"
        env["PYGAME_ANDROID"] = "TRUE"
        return env


recipe = PygameCeRecipe()
