# LRC - CRC verification generator

### This is a simple generator for creating LRC or CRC verification code.  

`Step1` Select the verification type and entering type for it.  

`Step2` Enter the address, functional_code and data, or consider them as a single one.    
        ( Other section will then be zero )  

`Step3` Get the verification code.  

* There is a limit that if entering odd number datas, it will automatically turn it to an even one.  

### Example cases :

>Select verification type - 1 for LRC / 2 for CRC : `1`  
>Select entering type - 1 for binary / 2 for hexadecimal : `1`  
>  
>Address:`00000001`  
>Functional code:`00000011`  
>Data:`100000000010000000000000001`
>
>The LRC code is :  `F6`
---
>Select verification type - 1 for LRC / 2 for CRC : `1`  
>Select entering type - 1 for binary / 2 for hexadecimal : `2`  
>  
>Address:`01`  
>Functional code:`03`  
>Data:`04010001`  
>  
>The LRC code is :  `F6`  
---
>Select verification type - 1 for LRC / 2 for CRC : `2`  
>Select entering type - 1 for binary / 2 for hexadecimal : `1`  
>
>Address:`00000001`  
>Functional code:`00000011`  
>Data:`100001000000100000000000000010`  
>
>The CRC code is : `6FF7`  
---
>Select verification type - 1 for LRC / 2 for CRC : `2`  
>Select entering type - 1 for binary / 2 for hexadecimal : `2`  
>
>Address:`01`  
>Functional code:`03`  
>Data:`21020002`  
>
>The CRC code is : `6FF7`  