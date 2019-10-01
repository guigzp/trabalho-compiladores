#!/bin/bash

# this is left as an example 
function compile() {
  if [ "$COMPILER" != "clang" ]; then
    parallel --tty --jobs=${JOBS} $COMPILER $COMPILE_FLAGS -S -c {} -o {.} ::: "${source_files[@]}"
  else
    # source_files is the variable with all the files we're gonna compile
    parallel --tty --jobs=${JOBS} $LLVM_PATH/$COMPILER $COMPILE_FLAGS \
      -Xclang -disable-O0-optnone \
      -w -S -c -emit-llvm {} -o {.}.bc ::: "${source_files[@]}" 
    
    parallel --tty --jobs=${JOBS} $LLVM_PATH/opt -S {.}.bc -o {.}.rbc ::: "${source_files[@]}"
  
    #Generate all the bcs into a big bc:
    $LLVM_PATH/llvm-link -S *.rbc -o $lnk_name
  
    # optimizations
    $LLVM_PATH/opt -S ${OPT} $lnk_name -o $prf_name

    # Compile our instrumented file, in IR format, to x86:
    $LLVM_PATH/llc -filetype=obj $prf_name -o $obj_name ;
    # Compile everything now, producing a final executable file:
    $LLVM_PATH/$COMPILER -lm $obj_name -o $exe_name ;
  fi
}
