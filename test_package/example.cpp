#include <restclient-cpp/connection.h>
#include <restclient-cpp/restclient.h>

int main()
{
    RestClient::init();
    RestClient::disable();
    return 0;
}
