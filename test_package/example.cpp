#include <gperftools/profiler.h>

#include <iostream>

int main() {
  ProfilerRestartDisabled();
  ProfilerEnable();
  ProfilerDisable();
  std::cout << "hi"
            << "\n";
}
