#include <restclient-cpp/connection.h>
#include <restclient-cpp/restclient.h>

int main()
{
    RestClient::init();
    RestClient::Connection conn{"https://url.com"};
    conn.SetTimeout(5);
    RestClient::disable();
    return 0;
}
