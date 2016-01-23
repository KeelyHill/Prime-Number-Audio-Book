# Prime Number Audio Book : 2<sup>74,207,281</sup> - 1

2<sup>74,207,281</sup> - 1 in audio form.

Takes in ogg files of individual numbers, then goes through the prime number(as a string from a file) and appends the sound bites together. Made a few days after 2<sup>74,207,281</sup> was confirmed as prime. The code is commented with some detail to help explain how it works.

Written with python 3.5.0. It will probably work with 3.x or 3.4.

**[Mersenne website](http://www.mersenne.org/primes/)**

## Requirements and Running

* [pydub](https://github.com/jiaaro/pydub), a python package
* ffmpeg installed on the system
* [pp (parallel python)](http://www.parallelpython.com) for splitting over cores

This was written on a machine with a 4 core CPU, this script uses ***2*** of those for parallel processing. This can be changed in the code. Assuming it is download in its own director and dependencies installed; run: `python prime_audio`

### ffmpeg
On Mac w/ Homebrew:
`brew install ffmpeg --with-libvorbis`
