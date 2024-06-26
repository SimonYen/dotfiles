# proxy [Address of proxy]
function proxyon
    set -Ux all_proxy http://$argv[(count $argv)]:7890
    set -Ux http_proxy http://$argv[(count $argv)]:7890
    set -Ux https_proxy http://$argv[(count $argv)]:7890
    set -Ux ALL_PROXY http://$argv[(count $argv)]:7890
    set -Ux HTTP_PROXY http://$argv[(count $argv)]:7890
    set -Ux HTTPS_PROXY http://$argv[(count $argv)]:7890
    echo all_proxy=$all_proxy
    echo http_proxy=$http_proxy
    echo https_proxy=$https_proxy
end

function proxyoff
    set -e all_proxy
    set -e http_proxy
    set -e https_proxy
    set -e ALL_PROXY
    set -e HTTP_PROXY
    set -e HTTPS_PROXY
end

