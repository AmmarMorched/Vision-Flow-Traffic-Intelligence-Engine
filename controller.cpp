#include <iostream>
#include <string>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    // Setup UDP Socket (listening on port 5005)
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    struct sockaddr_in servaddr;
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(5005);
    bind(sock, (const struct sockaddr *)&servaddr, sizeof(servaddr));

    char buffer[1024];
    struct sockaddr_in cliaddr;
    socklen_t len = sizeof(cliaddr);

    std::cout << "C++ Controller Waiting for Vision Data..." << std::endl;

    while (true) {
        int n = recvfrom(sock, buffer, 1024, 0, (struct sockaddr *)&cliaddr, &len);
        buffer[n] = '\0';
        int cars = std::stoi(buffer);

        // Simple Automation Logic
        if (cars > 5) {
            std::cout << "[ALGO] High Traffic (" << cars << " cars). Switching to LONG GREEN." << std::endl;
        } else {
            std::cout << "[ALGO] Normal Traffic. Standard Timing." << std::endl;
        }
    }
    return 0;
}