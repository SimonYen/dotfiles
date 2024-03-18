#rust相关环境变量设置

set -gx RUSTUP_DIST_SERVER https://rsproxy.cn
set -gx RUSTUP_UPDATE_ROOT https://rsproxy.cn/rustup

set -gx PATH "$HOME/.cargo/bin" $PATH
