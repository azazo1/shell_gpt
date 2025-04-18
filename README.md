# ShellGPT

这是 [ShellGPT](https://github.com/TheR1D/shell_gpt) 的一个 fork:
- [x] 按照指定语言输出.
- [x] 更短的 cli: `sm`, 且原有 `sgpt` 保留.
- [x] 直接使用 `sm how is it today?`, 而无需双引号包裹.

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
