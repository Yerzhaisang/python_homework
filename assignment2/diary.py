"""Append entries to diary.txt until the user enters the stop phrase."""

import traceback


# Task 1: Diary
def main():
    try:
        with open("diary.txt", "a", encoding="utf-8") as diary_file:
            prompt = "What happened today? "
            while True:
                line = input(prompt)
                diary_file.write(line + "\n")
                if line == "done for now":
                    break
                prompt = "What else? "
    except Exception as error:
        trace_back = traceback.extract_tb(error.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print("An exception occurred.")
        print(f"Exception type: {type(error).__name__}")
        message = str(error)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


if __name__ == "__main__":
    main()
