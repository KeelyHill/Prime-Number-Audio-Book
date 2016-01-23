'''
Desc: Compiles an audio clip of a string of numbers with the human voice.
Author: Keely Hill
MIT License

Scroll down to main() and processRangeForLines() for the action.
'''

from pydub import AudioSegment
import pp

number_sounds = []

def loadBigNumFileToList():
    print("Loading file.")
    with open('M74207281.txt') as f:
        lines = f.readlines()

    clean_lines = []

    for line in lines: # remove new-line-char to prevent problems
        clean_lines.append(line.strip('\n'))

    print("%i total lines!" % len(clean_lines))
    # return ['0','1','2','3','4','5','6','7','8','9'] # testing order
    return clean_lines


def processRangeForLines(range, lines, number_sounds):
    from pydub import AudioSegment # required here due to sending off in pp
    from datetime import datetime

    """helper func to translate string to sound"""
    def append_string_to_audio_segment(string, segment):
        for num in string:
            segment = segment + number_sounds[int(num)]
        return segment

    TOTAL_LINES = len(lines)
    TOTAL_LINES = 10
    PERCENT_DENOM = TOTAL_LINES / 5 # represents how often % status is reported

    audio = AudioSegment.empty() # init an output

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

    # get each sound as pydub audio segment and add to list for easy access
    for i in range(10):
        number_sounds.append(AudioSegment.from_ogg("sound_bites/%i.ogg" % i))

    # load in the beast by the lines of the file
    lines = loadBigNumFileToList()

    print("Creating blank audio file in memory.")
    output = AudioSegment.silent(duration=500) # 'blank' slate to append to.

    job_server = pp.Server()

    print("Splitting labor, and starting")
    # Define jobs, cpu cores/2 in my case
    #                                               give range    and other params
    job1 = job_server.submit(processRangeForLines, (range(0,10), lines, number_sounds))
    job2 = job_server.submit(processRangeForLines, (range(10,20), lines, number_sounds))

    # execute and grab value
    job1_audio = job1()
    job2_audio = job2()

    print("Final concatenation.")
    output += job1_audio + job2_audio

    print("Done making, now exporting... it make take a while.")
    file_handle = output.export("output.ogg", format="ogg", bitrate="64k", tags={"artist": "Keely Hill", "comments":"Made proudly."})
    print("\033[92m\033[1mComplete!\033[0m")


# Execution starts here with main()
if __name__ == '__main__':
    main()
