# 酒店管理系统 DEMO

## 需要的库

python 3
os
tkinter
PIL
sys
sqlite3
- [ ] ss
## 运行方法

1. `pip install -r requirements.txt`

2. 运行 main.py 即可

## 目录结构描述

```
.有用的内容
├── README.md              // 指南
├── requiremes.txt             // 库依赖
└── Starrt-Hotel-Management-System   // 核心代码
    ├── image                   // 文件src
    ├── hm_proj.db              // SQLite 数据库文件
    ├── login_system.py         // 登录系统
    ├── main.py                 // 主函数
    ├── MainRoot.py             // 主框架搭建文件
    └── test.txt                // 密码存储文档
```

### V1.0.1 版本内容更新

1. 修复已知 bug\*3
2. 优化界面美观度

### V1.0.2 版本内容更新

1. 修复了选择支付方式时扫过的按钮都会被选上的 bug 
2. 修复了无法正确存入”支付方式“属性的问题 
3. 修复了无法从数据库中正确获取”支付方式“属性的问题

### V1.1.1 版本内容更新

1. 增加了”登录“界面 
2. 增加了“正确将数据库中”房间数“等属性可视化”功能

### V1.1.2 版本内容更新

1. 修复了登录输入密码错误无惩罚的 bug，现在可以正常终止程序 
2. 改进了登录界面样式
