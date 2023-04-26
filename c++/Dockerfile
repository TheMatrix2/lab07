FROM ubuntu:18.04

RUN apt update
RUN apt install -yy gcc g++ cmake
RUN mkdir main
COPY . main/
WORKDIR main

RUN cmake -H. -B_build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=_install
RUN cmake --build _build
RUN cmake --build _build --target main

CMD ["_build/main"]