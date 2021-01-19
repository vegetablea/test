package main

import (
	"fmt"
	"github.com/golang/protobuf/proto"
	"net"
)

func main() {
	//1.建立监听端口
	listen, err := net.Listen("tcp", "0.0.0.0:20000")
	if err != nil {
		fmt.Println("listen failed, err:", err)
		return
	}

	fmt.Println("listen Start...:")

	for {
		//2.接收客户端的链接
		conn, err := listen.Accept()
		if err != nil {
			fmt.Printf("accept failed, err:%v\n", err)
			continue
		}
		//3.开启一个Goroutine，处理链接
		go process(conn)
	}
}

//处理请求，类型就是net.Conn
func process(conn net.Conn) {

	//处理结束后关闭链接
	defer conn.Close()
	for {
		var buf [128]byte
		n, err := conn.Read(buf[:])
		if err != nil {
			//fmt.Printf("read from conn failed, err:%v", err)
			break
		}
		data := &Students{}
		proto.Unmarshal(buf[:n], data)
		fmt.Printf("recv from client, content:%v\n", data)
		//fmt.Printf("recv from client, content:%v\n", string(buf[:n]))
	}

}