## Language information 
This program has been written in ARMv7 assembly language as on the Raspberry 
Pi. These can be purchased online for around £10-30. The starter set can be 
purchased for approximately £50.
## How to run
### Method 1 
1. Download or clone this GitHub repository 
2. (If downloaded) Extract the zip archive
3. Compile the .s file
```bash
as -o model.o model.s
```
4. Link the .o file(s)
- For a single .o file
```bash
ld -o model model.o
```
- For multiple files
```bash
ld -o model model.o myotherfile.o
```
5. Run the program 
```bash
./model
```
6. Display Register 0
```bash
echo $?
```
### Method 2
1. Download or clone this GitHub repository 
2. (If downloaded) Extract the zip archive
3. Run the program 
```bash
./model
```
4. Display Register 0
```bash
echo $?
```
## Debug the program 
1. Compile the .s file 
```bash
as -g -o model.o model.s
```
2. Link the .o files (as above) 
```bash
ld -o model model.o
```
3. Debug the program with 
```bash
gdb model
```
### Noteworthy commands
- List the next 10 lines: l
- Set breakpoint: b [line number]
- Run the program: r
- Continue to the next breakpoint: c
- Output register values: i r
- Run next line only: s
- Help: h
- Quit: q
