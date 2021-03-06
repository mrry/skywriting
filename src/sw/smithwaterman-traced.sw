// Library functions
include "grab";
//include "java";

function java(class_name, input_refs, argv, jar_refs, num_outputs) {
   f = env["FOO"];
	return spawn_exec("java", {"inputs" : input_refs, "class" : class_name, "lib" : jar_refs, "argv" : argv, "foo" : f, "stream_output": true, "debug_options":["trace_io"]}, num_outputs);
}  

// Numbers of blocks
num_rows = int(env["NUM_ROWS"]);
num_cols = int(env["NUM_COLS"]);

// Java code
java_lib = [grab("http://www.cl.cam.ac.uk/~cs448/SmithWaterman.jar")];

// Input data
url1 = env["INPUT1"];
url2 = env["INPUT2"];
horiz_source = *grab(url1);
vert_source = *grab(url2);

// -----------------------------------------

horiz_chunks = java("skywriting.examples.smithwaterman.PartitionInputString", horiz_source, [], java_lib, num_cols);
vert_chunks = java("skywriting.examples.smithwaterman.PartitionInputString", vert_source, [], java_lib, num_rows);

blocks = [];

blocks[0] = [];

blocks[0][0] = java("skywriting.examples.smithwaterman.SmithWaterman", [horiz_chunks[0], vert_chunks[0]], ["tl", -1, -1, -1, 2], java_lib, 3);
for (j in range(1, num_cols)) {
    blocks[0][j] = java("skywriting.examples.smithwaterman.SmithWaterman", [horiz_chunks[j], vert_chunks[0], blocks[0][j-1][2]], ["t", -1, -1, -1, 2], java_lib, 3);
}

i = 0;
j = 0;

for (i in range(1, num_rows)) {
    
    blocks[i] = [];

    blocks[i][0] = java("skywriting.examples.smithwaterman.SmithWaterman", [horiz_chunks[0], vert_chunks[i], blocks[i-1][0][1]], ["l", -1, -1, -1, 2], java_lib, 3);
    
    for (j in range(1, num_cols)) {
       blocks[i][j] = java("skywriting.examples.smithwaterman.SmithWaterman", [horiz_chunks[j], vert_chunks[i], blocks[i-1][j-1][0], blocks[i-1][j][1], blocks[i][j-1][2]], ["i", -1, -1, -1, 2], java_lib, 3);
    }

}

// -----------------------------------------

ignore = spawn_exec("sync", {"inputs":[blocks[i][j][0]]}, 1);

return *(ignore[0]);
