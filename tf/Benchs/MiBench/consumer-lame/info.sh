bench_name="consumer-lame"

source_files=( "VbrTag.c" "brhist.c" "common.c" "dct64_i386.c" "decode_i386.c" "fft.c" "formatBitstream.c" "get_audio.c" "gpkplotting.c" "gtkanal.c" "id3tag.c" "ieeefloat.c" "interface.c" "l3bitstream.c" "lame.c" "layer3.c" "main.c" "mpglib_main.c" "newmdct.c" "parse.c" "portableio.c" "psymodel.c" "quantize-pvt.c" "quantize.c" "reservoir.c" "rtp.c" "tabinit.c" "tables.c" "takehiro.c" "timestatus.c" "util.c" "vbrquantize.c" "version.c" )
COMPILE_FLAGS=" -lm -DHAVEMPGLIB -DLAMEPARSE -DNDEBUG -D__NO_MATH_INLINES -O -DLAMESNDFILE "
RUN_OPTIONS=" large.wav Output/output_large.mp3 "
