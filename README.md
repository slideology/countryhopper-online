# CountryHopper - 互动地理知识游戏

CountryHopper是一个基于网页的互动地理知识游戏平台，让用户可以在线测试和提高他们的地理知识。游戏主要通过嵌入的iframe加载，提供了一个有趣的方式来学习世界各国的地理位置和知识。

## 项目功能

- **互动地理游戏**：通过嵌入式游戏界面，用户可以参与地理知识挑战
- **用户账户系统**：支持用户注册、登录和个人资料管理
- **积分系统**：用户可以获取和使用积分
- **订阅和支付**：集成Stripe支付系统，支持多种付费计划
- **联系表单**：用户可以通过网站联系管理员

## 技术栈

- **后端**：Python Flask框架
- **数据库**：SQLAlchemy ORM，SQLite数据库
- **前端**：HTML, CSS, JavaScript, Tailwind CSS
- **支付处理**：Stripe API
- **部署**：支持Vercel部署

## 项目结构

```
countryhopper-online/
├── app.py                # 主应用入口，包含路由和视图函数
├── models.py             # 数据库模型定义
├── init_db.py            # 数据库初始化脚本
├── requirements.txt      # 项目依赖
├── .env.example          # 环境变量示例文件
├── static/               # 静态资源目录
│   ├── css/              # CSS样式文件
│   ├── js/               # JavaScript文件
│   └── images/           # 图片资源
├── templates/            # HTML模板
│   ├── base.html         # 基础模板
│   ├── index.html        # 首页模板
│   ├── game.html         # 游戏页面模板
│   ├── about.html        # 关于页面模板
│   ├── contact.html      # 联系页面模板
│   └── ...               # 其他模板文件
└── vercel.json           # Vercel部署配置
```

## 安装和运行

### 前提条件

- Python 3.8+
- pip (Python包管理器)

### 安装步骤

1. 克隆仓库：
   ```
   git clone git@github.com:slideology/countryhopper-online.git
   cd countryhopper-online
   ```

2. 创建并激活虚拟环境（推荐）：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用: venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

4. 创建环境变量文件：
   ```
   cp .env.example .env
   ```
   然后编辑`.env`文件，填入必要的环境变量（如SECRET_KEY、EMAIL配置、Stripe密钥等）

5. 初始化数据库：
   ```
   python init_db.py
   ```

6. 运行应用：
   ```
   python app.py
   ```

7. 在浏览器中访问：`http://localhost:3000`

## 环境变量配置

在`.env`文件中配置以下环境变量：

- `SECRET_KEY`：Flask应用的密钥
- `EMAIL_USER`：用于发送邮件的邮箱地址
- `EMAIL_PASSWORD`：邮箱密码或应用密码
- `STRIPE_SECRET_KEY`：Stripe支付API密钥
- `STRIPE_PUBLISHABLE_KEY`：Stripe公开密钥

## 数据库模型

项目使用SQLAlchemy ORM，主要模型包括：

- `User`：用户信息和认证
- `Message`：用户消息
- `ImageGeneration`：图像生成记录
- `Payment`：支付记录
- `Subscription`：订阅信息
- `PricingPlan`：价格计划

## 部署

项目支持通过Vercel部署，配置文件为`vercel.json`。

## 开发者注意事项

- 游戏内容通过iframe从itch.io加载
- 联系表单使用Gmail SMTP发送邮件
- 支付系统使用Stripe API处理

## 测试账户

系统初始化时会创建一个测试账户：
- 用户名：test
- 邮箱：test@example.com
- 密码：password

## 许可证

[项目许可证信息]
