<div align=center>
<img src="https://img.shields.io/badge/Author-szx-orange" alt="szx" /> <img src="https://img.shields.io/github/last-commit/s123456-max/zzuClock"/> <img src="https://img.shields.io/github/forks/s123456-max/zzuClock"/> <img src="https://img.shields.io/github/stars/s123456-max/zzuClock"/>
</div>

# zzuClock使用指南 :mega:（手写文字对应数字验证码+无验证码，每天凌晨两点自动打卡，邮件提醒）

## :bulb: 2022.12.25 打卡已结束，项目正式完结，见证了这一段历史。

## 2022.12.7 增加请求参数```ghdn28```

## 2022.10.15 执行的```unbuntu18.04```崩了，换成```macOS-latest```版本。

## 2022.9.10 当前可用。今天以后仓库停止更新，fork前请移步当前仓库actions看最新scheduled执行是否成功。

## 2022.9.9 增加了没有验证码的处理情况。

## 2022.9.7 测试结果（均已解决）：

1. 原来的调用接口识别不准确，出现了识别不准的情况，更换了专用的手写调用接口（不过仍有可能小概率识别失败）：

![图片](https://user-images.githubusercontent.com/59247205/189002498-c5da0108-bc38-48fa-857b-dfc4ee1b223c.png)

![图片](https://user-images.githubusercontent.com/59247205/189003503-23974747-de04-4d6e-a844-e54d5536d6aa.png)

---

![图片](https://user-images.githubusercontent.com/59247205/189008115-1d44d078-b5be-40e1-bb2f-fcf000a3d6f4.png)

2. 可能会有ssl问题（随机出现，定时执行两次任务中出现了一次，将unbutu操作系统降级为18.04，错误消失）

![图片](https://user-images.githubusercontent.com/59247205/189004494-138f30ae-44a2-49c7-b78f-5764d278eb6d.png)

## 0. 首先fork这个仓库 ↓

![图片](https://user-images.githubusercontent.com/59247205/188881805-fbfe06ff-e014-459b-9c38-e10dcb50e638.png)

## 1. 打开最右边的settings ↓

![图片](https://user-images.githubusercontent.com/59247205/188884799-ad763d53-180d-4d7b-ba70-fd0027cc474b.png)

## 2. 打开Secrets里的Actions ↓

![图片](https://user-images.githubusercontent.com/59247205/188790740-f21c7635-7863-4b55-a0a9-1a730a296c5b.png)

## 3. 点击New repository secret ↓

![图片](https://user-images.githubusercontent.com/59247205/188791007-9444de52-9b6e-40bb-ac10-2095b4bc0982.png)

## 4. 按下图所示添加参数 ↓

![图片](https://user-images.githubusercontent.com/59247205/188791770-6c7457af-b2a4-4c6b-8834-f862c3e9482e.png)

## 5. 同理，继续添加upw、email和city，一共四个参数 ↓

### 参数uid（学号）
> 示例：201984110513
### 参数upw（密码）
> 示例：123456
### 参数email（邮箱）
> 示例：1586924294@qq.com
### 参数city（城市代号）
> 示例：4101
- 4101 郑州市
- 4102 开封市
- 4103 洛阳市
- 4104 平顶山市
- 4105 安阳市
- 4106 鹤壁市
- 4107 新乡市
- 4108 焦作市
- 4109 濮阳市
- 4110 许昌市
- 4111 漯河市
- 4112 三门峡市
- 4113 南阳市
- 4114 商丘市
- 4115 信阳市
- 4116 周口市
- 4117 驻马店市
- 4118 济源市

## 6. 添加好后的示意图 ↓

![图片](https://user-images.githubusercontent.com/59247205/188792145-04bc7822-a4e2-46eb-b389-9840d5b4ad43.png)

> 到这里所有的配置已经完成，下面的内容选看 :tada: :tada: :tada:

## （立即触发，用于测试）7. 然后切换到Actions，选择zzuClock

![图片](https://user-images.githubusercontent.com/59247205/188794178-780c4315-3b4e-4818-a6d8-b6f50723cc12.png)

## （立即触发，用于测试）8. 点击Run workflow开始运行

![图片](https://user-images.githubusercontent.com/59247205/188794383-fb3d695c-feb4-4cde-9441-f2862a828310.png)

## （邮件提醒效果图）9. 自动打卡后的邮件提醒（每天凌晨两点自动打卡，应该会有一两个小时的延迟） ↓

![图片](https://user-images.githubusercontent.com/59247205/189049521-b26e1b9e-8542-4147-a0ae-097df04738a0.png)

## 完结! :boom: :boom: :boom:
