#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b, c;
    printf("Enter three sides of the triangle: ");
    scanf("%d %d %d", &a, &b, &c);
    if((a<0 || a>10) || (b<0 || b>10) || (c<0 || c>10)){
        printf("Out of Range values\n");
        exit(0);
    }
    
    // Check if the sides form a triangle
    if (a + b > c && a + c > b && b + c > a) {
        if (a == b && b == c) {
            printf("Equilateral Triangle\n");
        } else if ((a != b) || (b != c) || (a != c)) {
            printf("Isosceles Triangle\n");
        } else {
            printf("Scalene Triangle\n");
        }
    } else {
        printf("Triangle cannot be formed\n");
    }
    return 0;
}
