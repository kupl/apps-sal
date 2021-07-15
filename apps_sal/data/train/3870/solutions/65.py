def solve(s):
    reversed = s[::-1];
    reversed = "".join(reversed.split(" "));
    spaces = [];
    for i in range(len(s)):
        if s[i] == " ":
            spaces.append(i);
    result = "";
    spacesCount = 0;
    for i in range(len(s)):
        if i in spaces:
            result += " ";
            spacesCount += 1;
        else:
            result += reversed[i - spacesCount];
    return result;
