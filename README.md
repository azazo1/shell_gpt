# ShellGPT

这是 [ShellGPT](https://github.com/TheR1D/shell_gpt) 的一个 fork:
- [x] 按照指定语言输出.
- [x] 更短的 cli: `sm`, 且原有 `sgpt` 保留.
- [x] 直接使用 `sm how is it today?`, 而无需双引号包裹.
- [x] shell 命令输出支持修改, 见 [shell 命令](#shell-命令).
- [x] shell 命令输出支持复制而不执行.

## 安装

```shell
uv tool install https://github.com/azazo1/shell_gpt.git
```

## 配置

### 语言

`~/.config/shell_gpt/.sgptrc` 下修改:

```ini
TEXT_LANG=<your_language>
```

- `<your_language>` 可以任何形式提供, 它直接被传给模型, 此仓库未作提示词注入检查.

## 功能

### shell 命令

和原仓库相比, shell 命令的输出支持修改(`m` 选项), 直到模型输出了满足要求的命令之后才选择执行.

```shell
sm -s find all .json files in current folder
# -> find . -name "*.json"
# -> [E]xecute, [D]escribe, [A]bort, [M]odify, [C]opy: m
# -> >>> only in this folder, not including sub folders.
# -> find . -maxdepth 1 -name "*.json"
# -> [E]xecute, [D]escribe, [A]bort, [M]odify, [C]opy: e
# -> ...
```

也可以使用 c 选项直接复制命令而不修改:

```shell
sm -s find all .json files in current folder
# -> find . -name "*.json"
# -> [E]xecute, [D]escribe, [A]bort, [M]odify, [C]opy: c
```
