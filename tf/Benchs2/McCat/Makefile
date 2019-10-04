# MultiSource/McCat Makefile:  Build all subdirectories automatically

LEVEL = ../../..
PARALLEL_DIRS  := 04-bisect
ifdef BENCHMARKING_ONLY
PARALLEL_DIRS := $(filter-out 15-trie, $(PARALLEL_DIRS))
endif


include $(LEVEL)/Makefile.programs
