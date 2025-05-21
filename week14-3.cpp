//week14-3.cpp
#include <stdio.h>
int main()
{
	int n,ans=0;
	while(	scanf("%d", &n)==1){
		if(n==0)break;
		if(n>0)	ans+=n;
	}
	printf("%d",ans);
}
