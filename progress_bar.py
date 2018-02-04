import sys
def display_progress(idx, total):
    # 此函數的設計是要在迴圈內被重複呼叫 !!
    # idx : 進行任務的索引, 從 0 ~ total -1.
    # total : 要進行的任務次數

    # 當螢幕顯示 50 個 "=", 進度即抵達 100 %
    num_of_bar = 50

    # 計算一個進度單位
    unit = total / 100.0
    fprogress = " %3.2f"%((idx+1) / unit)

    # 計算有多少百分比已經完成
    done = int((idx+1) * num_of_bar / total)
    # 計算有多少百分比尚未未成
    not_yet = num_of_bar - done

    # 透過字串組合將結果連結起來
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
