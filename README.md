# combustible-brains
Official Repository for Combustible Brains

### Developer notes
* On Linux use `sudo` when running `docker`.
* Audio `/audio` folder now uses `docker`.
* Ensure that your audio files are placed in the container folder (/audio), prior ot building the docker container.
* When updating audio, use `docker build -t podcast-helper .`
* To use the helper, use `docker run podcast-helper <mp3 file name>`