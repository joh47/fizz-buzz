def fizz_buzz(map, start, end):
    if isinstance(map, dict) and isinstance(start, int) and isinstance(end, int) and start < end:
        for value in range(start, end + 1):
            output = ""
            for key in map:
                if value % int(key) == 0:
                    output += map[key]
            if output == "":
                output = value
            print(output)
    else:
        raise Exception("CallError: fizz_buzz expects arguments of (map [dict], start [int], end [int]) where start < end")

map = {"3":"Fizz", "5":"Buzz"}
start = 1
end = 100

fizz_buzz(map, start, end)
