# TODO:
# This script needs to provide the the features listed below.
# These features will be added incrementally.

# Initial approach:
# 1. Copy the mtb-lib.a static library to the corresponding variant board directory. 
#    - From build/mtb-libs.a to variants/$board/mtb-libs.a
# Later approach:
# 1. Copy the required sources to the cores/ directory to let the Arduino toolchain compile the sources.

# 2. Generate and copy the required C/CXX build flags in the corresponding variant board directory.
#    - Parse .cycompiler to extract required flags.
#    - These flags don´t need any additional processing.
#    - Copy to variants/$board/mtb-lib-cxx-flags.txt
# 3. Generate and copy the required linker flags in the corresponding variant board directory.
#    - Parse .cylinker to extract required flags.
#    - The linker script path needs to be to be substituted to the corresponding Arduino core path !!! This will require some append in platform.txt hook later anyhow!
#    - Copy to variants/$board/mtb-lib-linker-flags.txt
# 4. Generate and copy the required include paths in the corresponding variant board directory.
#    - Parse inclist.rsp to extract required paths.
#    - Substitute the paths to the corresponding Arduino core paths !!! This will require some append in platform.txt hook later anyhow!
#       - bsp/APP_TARGET folder should be now in variants (symlinked)
#           - We need to remove each COMPONENT_ not used, and each TOOLCHAIN_ dirs not used (God kill me!)
#       - Each mtb_shared library should be externally added as a submodule (not as mtb_shared).
#           - mtb_shared libraries should be now in extras/ folder. 
#       - Modify the path to that library also removing the version. Let´s see in the future if we need a version per bsp, but that should not be the case.
#           - ../mtb_shared/$library/release-vx.y.z/ --> extras/$library
#       - These submodules libs in extras/ will also be released with the core package.
#    - Copy to variants/$board/mtb-lib-includes.txt
# 5. Select the required libraries which need to be included in the arduino-core-psoc and track their versions against the mtb-lib.a used versions.