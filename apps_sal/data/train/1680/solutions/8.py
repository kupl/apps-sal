# include <stdio.h>
# include <string.h>
# include <stdlib.h>

void main()
{
 int i, n, v, s, len1, len2, len;
 char s1[210], s2[210], output[210];
 
 scanf("%d",&n);
 while(n--)
 {
   scanf("%s%s",s1,s2);
   memset(output,'\0',sizeof(output));
   len1 = strlen(s1);
   len2 = strlen(s2);
   len = len1>len2?len1:len2;
   while(len1<=len)
    s1[len1++] = '0';
    s1[len1]='\0';
   while(len2<=len)
    s2[len2++] = '0';
    s2[len2]='\0';
   v = 0;
   for(i = 0; i <= len; i++)
   {
    s = (s1[i]+s2[i]-96+v)%10;
    v = (s1[i]+s2[i]-96+v)/10;
    output[i] = s+48;
   }
   if(output[len]=='0') output[len]='\0';
   for(i = 0; i <= len; i++)
   if(output[i]!='0'&&output[i]!='\0')
   {strcpy(output,&output[i]);break;}
   puts(output);
   }
}


