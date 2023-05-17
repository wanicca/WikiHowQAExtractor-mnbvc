# WikiHowQAExtractor-mnbvc

[English Version](README-EN.md)

## 项目描述

- 本项目主要目的是从WikiHow页面抽取中文/英文问答数据。
- 可接受的输入为一组HTML文件。或者是一个csv文件，其中`html`列保存了多个页面的HTML代码。
- 处理结果为jsonl文件，每行对应一个词条页面，包含问答文本，以及可供参考的词条结构，详细格式附后。

## 环境

1. 下载本项目
```
git clone WikiHowQAExtractor-mnbvc
```
2. 进入目录并安装依赖
```
cd WikiHowQA-mnbvc
pip install -r requirements.txt
```

## 用法

通过以下命令将FILE1 FILE2 等输入HTML文件转化并输出到以`wikihow`为名称的结果文件中。
```shell
python wikihow_extract.py FILE1 FILE2 ... -o wikihow
```

或者，当有多个html文件代码存储在单个csv文件中时，使用以下命令转化并输出。

```shell
python wikihow_extract.py -c CSVFILE -o wikihow
```

以上两种命令将会输出结果文件`wikihow.0.jsonl`，当结果文件大于件500MB时会分块处理，产生`wikihow.1.jsonl`、`wikihow.2.jsonl`等。

## 注意

1. 本工具会自动跳过无法解析出问题和解决方法的页面，比如已删除页面、分类页面、管理页面。
2. 暂时未保留图片信息。

## 代码说明

- `wikihow_extract.py` 入口程序
- `wikihow_parser.py` Wikihow页面解析器，基于Beautifulsoup 


## 输出jsonl文件格式

1. 每行为一个jsonl文件，每行是一条问答数据，对应一个WikiHow词条页面。
2. 对于每一个问答数据，其最高层次结构如下。
```json
{
    "id":123456
    "问":"写一个超短小说",
    "答":"他们相遇，又别离。岁月如梭，情感却不减。",
    "指令":"generate story",
    "来源":"wikihow",
    "元数据":{
        "create_time":"20230511 15:56:03",
        "问题明细":"",
        "回答明细":"",
        "扩展字段":""
    }
}
```
3. 在wikihow语料中，`"回答明细"`是一个列表,结构层次如下：
```json
[
    {
    "回答": "完整回答文本，包含方法、提示、注意事项",
    "简要回答": "回答的摘要文本，来自WikiHow的页面开头信息，概括了页面的主要内容",
    "结构": {}
    }
]
```
4. 每个回答除了回答文本、简要回答文本以外，还有可供参考使用的结构信息，该对象的结构如下。
```json
"结构": {
    "方法":[],
    "小提示":[],
    "注意事项":[]
}
```
5. 方法内部的结构包括编号、标题、步骤，每个步骤包括自己的编号、标题、描述，具体可参考下面的结果示例。
6. 小提示、注意事项为字符串列表，没有更进一步的结构。

## 结果示例

```json
{
  "问题": "如何在PS3上玩PS2游戏",
  "回答": [
    {
      "回答": "1. 了解基础知识\n1-1. 查明你的PS3是否具有反向兼容性。\nPS3游戏机经历了一系列的更新升级和改变。尽管有些版本的PS3控制台可用于玩PS2游戏，但是并不是所有版本都 能够兼容。\n通常情况下，旧版本的游戏控制台可以用于玩PS2游戏，但是为了节约生产成本、保证PS3游戏的购买量，索尼公司削减了该项功能，从而导致新版本的控制台无法兼容PS2游戏。\n你可以查看游戏机机型和序列号，来确定 其是否具有反向兼容性。这些信息一般位于底部的条形码贴纸上或控制台的背部。机器序列码是有11位数字组成的数字串。\nCECH-Axx和CECH-Bxx机器（型号分别是60 GB和20 GB）是完全兼容PS2光盘游戏的。CECH-Cxx和CECH-Exx机器 （60 GB和80 GB机型）部分兼容PS2。\nG、H、J、K、L、M、P和Q机型的非轻薄版机器不兼容PS2游戏。\n所有轻薄版PS3机器都不兼容PS2游戏。\n1-2. 像往常那样，插入游戏光盘。\nPS2光盘插入光驱的方法和PS3光盘相同。一旦插入 光盘，无需其它动作指令或协助，PS3就会自动识别并载入光盘内容。 接着，你就可以玩你想玩的游戏了。\n2. 在PS3上存档PS2游戏\n2-1. 前往PS3存储卡管理程序 。\n为了在PS3上存档游戏，你需要在机器硬盘中创建一个内存卡。\ n插入光盘后，在游戏选项菜单中选择“游戏”，然后选择“存储卡程序（PS/PS2）”。\n存储卡容量限制为8 MB。\n2-2. 选择“新建内存卡”。\n你也可以将一个现有的记忆卡卡槽分配给PS2游戏，但是如果没有现成的卡槽，你可以新建一 个。\n2-3. 选择“内存卡（PS2）”。\n不要选择“内存卡（PS）”选项，因为它会创建一个用于原始的PS游戏的内存卡槽，而不是PS2游戏。\n2-4. 更改名称。\n选择底部的名称并使名称一栏高亮显示。此时，屏幕上会出现一个键盘，你 可以拼写任意名称来命名存储卡。输入名称，并选择“确定”。\n2-5. 点击“选择”按钮。\n这就将新的内存卡分配到卡槽1，也就是按顺序排好的第一个可用卡槽。\n3. 指定一个现有的记忆卡卡槽\n3-1. 打开PS3存储卡管理程序。\n在 游戏选项菜单中选择“游戏”，然后选择“存储卡程序（PS/PS2）”。按下“选择”按钮来继续操作。\n除了用于创建新的内存卡，存储卡管理程序还可用于将PS2游戏分配到之前创建的PS2存储卡。\n3-2. 找到你想使用的记忆卡。\n浏览现 有的内存卡，找到空的或者你想要覆盖的存储卡。高亮标记它，并点击“选择”按钮。\n3-3. 选择“分配卡槽”选项。\n这个选项会出现在屏幕上方或一侧的菜单中。或者，当你选中卡槽后它会出现在卡槽一侧。当你找到该选项后，高亮 选择它，并按下“选择”按钮。\n3-4. 指定卡槽。\n你可以看到“卡槽1”或“卡槽2”这样的选项。高亮选择其中一个选项，并按下手柄上的“选择”按钮来分配内存卡卡槽。\n如果你想要将内存卡移除卡槽，你可以按照上述方法选中它，并 选择屏幕菜单中的“移除”选项。\n如果你的PS3控制台不兼容，那么可以尝试从Playstation在线商店下载PS2版本游戏。遇到这种情况时，你需要购买一个新游戏，而不是使用旧版本游戏。但在兼容的控制台上也可以玩旧版本游戏。\n 值得注意的是，有些PS2游戏只能部分兼容于PS3设备，所以在玩游戏的过程中可能遭遇各种问题。以下将列出部分于PS3设备的游戏：\n\n生死极速\n魔力女战士\n火爆狂飙\n极度深寒\n圣剑传说\n异星毁灭者\n战神\n枪墓\n詹姆斯邦 德007：夜火\n街头橄榄球 3\n影之心：契约\n影之心：来自新世界\n深渊传说\n变形金刚\nYakuza\n",
      "简要回答": "如果你的PS3游戏机的机型在硬件上兼容PS2光盘，那么你就可以在PS3上正常地玩PS2的游戏。尽管存档这些游戏需 要额外的步骤，但是一旦你完成相关的游戏设置，很快你就可以在PS3上玩PS2游戏啦。",
      "结构": {
        "方法": [
          {
            "编号": 1,
            "标题": "了解基础知识",
            "步骤": [
              {
                "编号": 1,
                "标题": "查明你的PS3是否具有反向兼容性。",
                "描述": " PS3游戏机经历了一系列的更新升级和改变。尽管有些版本的PS3控制台可用于玩PS2游戏，但是并不是所有版本都能够兼容。\n通常情况下，旧版本的游戏控制台可以用于玩PS2游戏，但是为了节约生产成本、保证PS3游戏的购买量，索 尼公司削减了该项功能，从而导致新版本的控制台无法兼容PS2游戏。\n你可以查看游戏机机型和序列号，来确定其是否具有反向兼容性。这些信息一般位于底部的条形码贴纸上或控制台的背部。机器序列码是有11位数字组成的数字串 。\nCECH-Axx和CECH-Bxx机器（型号分别是60 GB和20 GB）是完全兼容PS2光盘游戏的。CECH-Cxx和CECH-Exx机器（60 GB和80 GB机型）部分兼容PS2。\nG、H、J、K、L、M、P和Q机型的非轻薄版机器不兼容PS2游戏。\n所有轻薄版PS3机 器都不兼容PS2游戏。"
              },
              {
                "编号": 2,
                "标题": "像往常那样，插入游戏光盘。",
                "描述": "PS2光盘插入光驱的方法和PS3光盘相同。一旦插入光盘，无需其它动作指令或协助，PS3就会自动识别并载入光盘内容。 接着，你就可以玩你 想玩的游戏了。"
              }
            ]
          },
          {
            "编号": 2,
            "标题": "在PS3上存档PS2游戏",
            "步骤": [
              {
                "编号": 1,
                "标题": "前往PS3存储卡管理程序 。",
                "描述": "为了在PS3上存档游戏，你需要在机器硬盘中创建一个内存卡。\n插入光盘后，在游戏选 项菜单中选择“游戏”，然后选择“存储卡程序（PS/PS2）”。\n存储卡容量限制为8 MB。"
              },
              {
                "编号": 2,
                "标题": "选择“新建内存卡”。",
                "描述": "你也可以将一个现有的记忆卡卡槽分配给PS2游戏，但是如果没有现成的卡槽，你可以 新建一个。"
              },
              {
                "编号": 3,
                "标题": "选择“内存卡（PS2）”。",
                "描述": "不要选择“内存卡（PS）”选项，因为它会创建一个用于原始的PS游戏的内存卡槽，而不是PS2游戏。"
              },
              {
                "编号": 4,
                "标题": "更改名称。",
                "描述": "选择 底部的名称并使名称一栏高亮显示。此时，屏幕上会出现一个键盘，你可以拼写任意名称来命名存储卡。输入名称，并选择“确定”。"
              },
              {
                "编号": 5,
                "标题": "点击“选择”按钮。",
                "描述": "这就将新的内存卡分配到卡槽1，也就是按 顺序排好的第一个可用卡槽。"
              }
            ]
          },
          {
            "编号": 3,
            "标题": "指定一个现有的记忆卡卡槽",
            "步骤": [
              {
                "编号": 1,
                "标题": "打开PS3存储卡管理程序。",
                "描述": "在游戏选项菜单中选择“游戏”，然后选择“存储卡程序（PS/PS2）”。 按下“选择”按钮来继续操作。\n除了用于创建新的内存卡，存储卡管理程序还可用于将PS2游戏分配到之前创建的PS2存储卡。"
              },
              {
                "编号": 2,
                "标题": "找到你想使用的记忆卡。",
                "描述": "浏览现有的内存卡，找到空的或者你想要 覆盖的存储卡。高亮标记它，并点击“选择”按钮。"
              },
              {
                "编号": 3,
                "标题": "选择“分配卡槽”选项。",
                "描述": "这个选项会出现在屏幕上方或一侧的菜单中。或者，当你选中卡槽后它会出现在卡槽一侧。当你找到该选项后，高亮选 择它，并按下“选择”按钮。"
              },
              {
                "编号": 4,
                "标题": "指定卡槽。",
                "描述": "你可以看到“卡槽1”或“卡槽2”这样的选项。高亮选择其中一个选项，并按下手柄上的“选择”按钮来分配内存卡卡槽。\n如果你想要将内存卡移除卡槽，你 可以按照上述方法选中它，并选择屏幕菜单中的“移除”选项。"
              }
            ],
            "小提示": [
              "如果你的PS3控制台不兼容，那么可以尝试从Playstation在线商店下载PS2版本游戏。遇到这种情况时，你需要购买一个新游戏，而不是使用旧版本游戏。 但在兼容的控制台上也可以玩旧版本游戏。\n"
            ],
            "注意事项": [
              "值得注意的是，有些PS2游戏只能部分兼容于PS3设备，所以在玩游戏的过程中可能遭遇各种问题。以下将列出部分于PS3设备的游戏：\n\n生死极速\n魔力女战士\n火爆 狂飙\n极度深寒\n圣剑传说\n异星毁灭者\n战神\n枪墓\n詹姆斯邦德007：夜火\n街头橄榄球 3\n影之心：契约\n影之心：来自新世界\n深渊传说\n变形金刚\nYakuza\n"
            ]
          }
        ]
      }
    }
  ]
}
```

## 相关项目

[MNBVC](https://github.com/esbatmop/MNBVC)
[wikiHowUnofficialAPI](https://github.com/vigilant-umbrella/wikiHowUnofficialAPI)
