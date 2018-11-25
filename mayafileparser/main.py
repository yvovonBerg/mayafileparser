import os
import shutil
import re
import argparse

class MayaCommander(object):
    def __init__(
        self,
        maya_file
    ):
        self.file = maya_file
        self.contents = []
        self._safe_copy()
        self._load_file()
    
    def _safe_copy(self):
        out_directory = os.path.dirname(self.file)
        filename = os.path.basename(self.file).split('.')[0]
        new_file = os.path.join(
            out_directory, "{}_mayacommander.ma".format(filename)
        )
        shutil.copy(self.file, new_file)
        self.file = new_file

    def _load_file(self):
        if not os.path.exists(self.file):
            print "{} does not exist".format(self.file)
            sys.exit()
        
        if '.ma' not in self.file:
            print "only .ma is supported"
            sys.exit()

        print "parsing maya scene"
        with open(self.file, 'r') as m_file:
            self.contents = m_file.readlines()
    
    def _write_file(self):
        with open(self.file, 'w') as m_file:
            m_file.writelines(self.contents)
        print "done: {}".format(self.file)

    def disable_node(self, search_string, block_mode):
        new_file_contents = []
        comment_modus = False
        for maya_line in self.contents:
            new_line = maya_line
            if search_string in maya_line:
                # found match in line
                if not block_mode:
                    # ignore this line
                    continue

                if not comment_modus:
                    # make comment setting stick
                    comment_modus = True
                    continue
                
                if comment_modus:
                    # ignore this line
                    continue
            
            # disable attributes from node
            elif comment_modus and r'\t' in repr(new_line):
                continue

            if r'\t' not in repr(new_line):
                comment_modus = False

            new_file_contents.append(new_line)           
        self.contents = new_file_contents
        self._write_file()

def _parse_arguments():
    parser = argparse.ArgumentParser(
        description='Maya command line file parsing',
    )
    parser.add_argument('--file', help='.ma filepath')
    parser.add_argument('--mode', help='mode')
    parser.add_argument('--command', help='command')
    parser.add_argument('--block_mode', help='block indent mode')

    return parser.parse_args()


if __name__ == "__main__":
    
    args = _parse_arguments()
    mc = MayaCommander(
        maya_file=args.file
    )
    if args.mode == "disable_node":
        mc.disable_node(
            search_string=args.command,
            block_mode=args.block_mode
        )
