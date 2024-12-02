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


import argparse, os

version = "0.1.0"

def add_bsp(board, dest_dir=None, copy=False):

    # Check if board BSP exists
    # If not, print error message and return
    if not os.path.exists(os.path.join("bsps", "APP_TARGET_" + board)):
        print("Error: Board BSP not found")
        return

    # Check if dest_dir is provided
    # Otherwise, set the default value    
    if dest_dir is None:
        dest_dir = os.path.join("variants", board, "mtb-bsp")

    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get destination directory
        
    # Get the a list of the include and exclude files and 
    # directories to be copied to the destination
    
        
    # Copy the files and directories to the destination directory
        
    # Generate report file with traceable info of 
    # the copied files and directories

def parser():

    def main_parser_func(args):
        parser.print_help()

    def parser_add_bsp_func(args):
        add_bsp(args.board, args.dest_dir, args.c)

    # Main parser
    class ver_action(argparse.Action):
        def __init__(self, option_strings, dest, **kwargs):
            return super().__init__(
                option_strings, dest, nargs=0, default=argparse.SUPPRESS, **kwargs
            )

        def __call__(self, parser, namespace, values, option_string, **kwargs):
            print("mtb-integration version: " + version)
            parser.exit()

    parser = argparse.ArgumentParser(description="ModusToolbox Arduino PSOC Core Integration Utility")
    parser.add_argument("-v", "--version", action=ver_action, help="mtb-integration version")
    subparser = parser.add_subparsers()
    parser.set_defaults(func=main_parser_func)

    # Add bsp parser 
    parser_add_bsp_desc='''
    Add the MTB board BSP sources to the variant/<board> core directory.

    Details: 

    The relevant files and folders of
    "mtb-arduino-core-psoc-integration/bsps/APP_TARGET_board>"  
    directory will be symlinked to 
    "variants/<board>/mtb-bsp" directory.

    The directory cannot be entirely copied due to the lack of 
    sources exclusion mechanism of the Arduino build toolchain.
    Only some of the directories prefixes with "COMPONENT_" and
    "TOOLCHAIN_" will are required, thus only those will be linked.

    Additionally, only ModusToolbox relevant metafiles (i.e. 
    .cyignore, deps/, ...) and docs will also be excluded. 

    '''
    parser_add_bsp = subparser.add_parser("add-bsp", formatter_class=argparse.RawTextHelpFormatter, description=parser_add_bsp_desc)
    parser_add_bsp.add_argument("board", type=str, help="Board (BSP) name")
    parser_add_bsp.add_argument("-d", "--dest-dir", type=str, help="Destination dir for the bsp sources. Default: variants/<board>/mtb-bsp") 
    parser_add_bsp.add_argument("-c", action="store_true", help="Copy the bsp files instead of creating symbolic links")
    parser_add_bsp.set_defaults(func=parser_add_bsp_func)

    # Parser call
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    parser()
