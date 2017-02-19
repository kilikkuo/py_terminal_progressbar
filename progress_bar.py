import sys
def display_progress(idx, total):
    # idx : from 0 to total - 1
    # total : The number of proceeding tasks.

    # How many "=" will be displayed when 100 % is achieved.
    num_of_bar = 50

    # Should be inside a loop, total should be fixed ! idx starts from 0
    unit = total / 100.0
    fprogress = " %3.2f"%((idx+1) / unit)

    done = int((idx+1) * num_of_bar / total)
    not_yet = num_of_bar - done

    sys.stdout.write("\r[" + "="*done +  " "*not_yet + "]" + fprogress + "%")
    sys.stdout.flush()

def test_display_progress(total):
    import time
    for i in range(total):
        time.sleep(0.01)
        display_progress(i, total)
    print("\n")

"""
#############################################################################
$> python3 progress_bar.py
"""
if __name__ == '__main__':
    test_display_progress(200)
