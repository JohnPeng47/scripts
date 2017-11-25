all: nasm link exec #first line is executed with just make
	
nasm: hello.asm
	@nasm -f elf64 hello.asm
link: hello.o
	@ld -s -o hello hello.o
exec:
	@./hello
clean:
	rm hello.o hello
