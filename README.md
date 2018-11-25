# mayafileparser

Simple parser to hide nodes from Maya ascii (.ma) files e.g.:  
<i>python main.py --file test.ma --mode disable_node --command pSphere --block_mode True</i>

<i>--file</i> : (test.ma) input maya ascii file, will be duplicated for safety.  
<i>--mode</i> : (disable_node) default for now.  
<i>--command</i> : (str) argument / search string for the node name you are trying to hide.  
<i>--block_mode</i> : (True/False)hide all attributes that are part of this node as well.  
