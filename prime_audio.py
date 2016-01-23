'''
Desc: Compiles an audio clip of a string of numbers with the human voice.
Author: Keely Hill
MIT License

Scroll down to main() and processRangeForLines() for the action.
'''

from pydub import AudioSegment
from datetime import datetime
import pp

number_sounds = []

def loadBigNumFileToList():
    print("Loading file.")
    with open('M74207281.txt') as f:
        lines = f.readlines()

    clean_lines = []

    for line in lines:
        clean_lines.append(line.strip('\n'))

    print("%i total lines!" % len(clean_lines))
    # return ['0','1','2','3','4','5','6','7','8','9'] # testing order
    return clean_lines


def processRangeForLines(range, lines, number_sounds):
    from pydub import AudioSegment
    from datetime import datetime

    def append_string_to_audio_segment(string, segment):
        for num in string:
            segment = segment + number_sounds[int(num)]
        return segment

    TOTAL_LINES = len(lines)
    TOTAL_LINES = 10
    PERCENT_DENOM = TOTAL_LINES / 5 # represents how often % status is reported

    audio = AudioSegment.empty()

    counter = 0
    for i in range:
        line = lines[i]

        counter += 1
        if counter % PERCENT_DENOM == 0:  # prints a % status every so often
             print(round((counter/TOTAL_LINES) * 100), "%% concatenating.",  datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        audio = append_string_to_audio_segment(line, audio)
    return audio


def main():

    print("Gettings raw number sound bites.")

    for i in range(10):
        number_sounds.append(AudioSegment.from_ogg("sound_bites/%i.ogg" % i))

    lines = loadBigNumFileToList()

    print("Creating blank audio file in memory.")
    output = AudioSegment.silent(duration=500)

    job_server = pp.Server()

    print("Splitting labor, and starting")
    # Define jobs, cpu cores/2 in my case
    job1 = job_server.submit(processRangeForLines, (range(0,5), lines, number_sounds))
    job2 = job_server.submit(processRangeForLines, (range(5,10), lines, number_sounds))

    job1_audio = job1()
    job2_audio = job2()

    print("Final concatenation.")
    output += job1_audio + job2_audio

    print("Done making, now exporting... it make take a while.")
    file_handle = output.export("output.ogg", format="ogg", bitrate="64k", tags={"artist": "Keely Hill", "comments":"Made proudly."})
    print("\033[92m\033[1mComplete!\033[0m")



if __name__ == '__main__':
    main()
