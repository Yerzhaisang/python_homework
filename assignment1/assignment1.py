# Task 1: Hello

def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String

def greet(name):
    return "Hello, " + name + "!"

# Task 3: Calculator

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operation} those values!"


# Task 4: Data Type Conversion

def data_type_conversion(value, dtype):
    try:
        if dtype == "float":
            return float(value)
        elif dtype == "str":
            return str(value)
        elif dtype == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {dtype}."

# Task 5: Grading System, Using *args

def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range

def repeat(string, count):
    result = ""

    for _ in range(count):
        result += string

    return result

# Task 7: Student Scores, Using **kwargs

def student_scores(operation, **kwargs):
    if operation == "best":
        best_student = None
        best_score = None

        for student, score in kwargs.items():
            if best_score is None or score > best_score:
                best_student = student
                best_score = score

        return best_student

    elif operation == "mean":
        return sum(kwargs.values()) / len(kwargs)

# Task 8: Titleize, with String and List Operations

def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)

# Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

# Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0

            while i < len(word):
                if word[i:i + 2] == "qu":
                    i += 2
                    break
                elif word[i] in vowels:
                    break
                else:
                    i += 1

            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)