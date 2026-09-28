[app]

title = Tic-Tac-Toe
package.name = tictactoe
package.domain = org.vanyaaegis
version = 1.0.0

source.dir = .
source.include_exts = py,json,txt,png,jpg,jpeg,ttf,wav
source.exclude_dirs = bin,tests,.git,.buildozer,p4a-recipes

requirements = python3,pygame-ce

orientation = portrait
fullscreen = 1

android.api = 35
android.minapi = 23
android.ndk = 27c
android.ndk_api = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
android.private_storage = True

# pygame-ce is supplied by the local python-for-android recipe below.
p4a.branch = develop
p4a.local_recipes = ./p4a-recipes

[buildozer]
log_level = 2
warn_on_root = 1
