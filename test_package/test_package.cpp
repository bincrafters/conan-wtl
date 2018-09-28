#include <cstdlib>
#include <iostream>

#include <atlbase.h>
#include <atlapp.h>
#include <atlmisc.h>

int main()
{
    std::cout << ATL::CString("Hello from WTL!") << std::endl;
    return EXIT_SUCCESS;
}
