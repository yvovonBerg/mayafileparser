# mayafileparser

Simple parser to hide nodes from Maya ascii (.ma) files.
e.g:
python main.py --file test.ma --mode disable_node --command pSphere --block_mode True

--file input maya ascii file, will be duplicated for safety
--mode disable_node default for now
--command argument / search string for the node name you are trying to hide
--block_mode hide all attributes that are part of this node as well
