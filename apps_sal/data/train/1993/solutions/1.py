class CursorStatus:
     NOT_IN_COMMENT = 0
     FIRST_BACKSLASH = 1
     INLINE_COMMENT_START = 2
     MULTILINE_COMMENT_START = 3
     FIRST_STAR_IN_MULTILINE_COMMENT = 4
 
 
 class Solution:
     def removeComments(self, source):
         """
         :type source: List[str]
         :rtype: List[str]
         """
         resultList = []
         status = CursorStatus.NOT_IN_COMMENT
         print(source)
         for line in source:
             if status != CursorStatus.MULTILINE_COMMENT_START:
                 result_line = ""
             temp = ""
             for ch in line:
                 if status == CursorStatus.NOT_IN_COMMENT:
                     if ch == '/':
                         status = CursorStatus.FIRST_BACKSLASH
                         temp = temp + ch
                     else:
                         result_line = result_line + ch
                 elif status == CursorStatus.FIRST_BACKSLASH:
                     if ch == '/':
                         status = CursorStatus.INLINE_COMMENT_START
                         temp = ""
                     elif ch == '*':
                         status = CursorStatus.MULTILINE_COMMENT_START
                         temp = ""
                     else:
                         status = CursorStatus.NOT_IN_COMMENT
                         temp = temp + ch
                         result_line = result_line + temp
                         temp = ""
                 elif status == CursorStatus.INLINE_COMMENT_START:
                     status = CursorStatus.NOT_IN_COMMENT
                     break
                 elif status == CursorStatus.MULTILINE_COMMENT_START:
                     if ch == '*':
                         status = CursorStatus.FIRST_STAR_IN_MULTILINE_COMMENT
                 elif status == CursorStatus.FIRST_STAR_IN_MULTILINE_COMMENT:
                     if ch == '/':
                         status = CursorStatus.NOT_IN_COMMENT
                     elif ch == '*':
                         status = CursorStatus.FIRST_STAR_IN_MULTILINE_COMMENT
                     else:
                         status = CursorStatus.MULTILINE_COMMENT_START
 
             if result_line != "" and status != CursorStatus.MULTILINE_COMMENT_START:
                 #print(result_line)
                 result_line = result_line + temp
                 resultList.append(result_line)
         print(resultList)
         return resultList
