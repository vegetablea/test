package main

import (
	"fmt"
	"github.com/golang/protobuf/proto"
	"net"
)

func main() {
	//1.建立一个链接（Dial拨号）
	conn, err := net.Dial("tcp", "0.0.0.0:20000")
	if err != nil {
		fmt.Printf("dial failed, err:%v\n", err)
		return
	}

	//fmt.Println("Conn Established...:")
	//
	////读入输入的信息
	s1:=&Student{} //第一个学生信息
	s1.Name="jz01"
	s1.Age=23
	s1.Address="cq"
	s1.Cn=ClassName_class2 //枚举类型赋值
	ss:=&Students{}
	ss.Person=append(ss.Person,s1) //将第一个学生信息添加到Students对应的切片中
	//buffer, _ := proto.Marshal(ss)
	//reader := bufio.NewReader(os.Stdin)
	for {
		data, err := proto.Marshal(ss)
		if err != nil {
			fmt.Printf("read from console failed, err:%v\n", err)
			break
		}

		//data = strings.TrimSpace(data)
		//传输数据到服务端
		_, err = conn.Write([]byte(data))
		break
		if err != nil {
			fmt.Printf("write failed, err:%v\n", err)
			break
		}
	}
}