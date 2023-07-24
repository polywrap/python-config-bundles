"""This module contains the configuration for the system bundle."""
from typing import Dict

from polywrap_core import Uri
from polywrap_fs_plugin import file_system_plugin
from polywrap_http_plugin import http_plugin
from polywrap_uri_resolvers import ExtendableUriResolver

from .embeds import get_embedded_wrap
from .types import BundlePackage

sys_bundle: Dict[str, BundlePackage] = {
    "http": BundlePackage(
        uri=Uri.from_str("plugin/http@1.1.0"),
        package=http_plugin(),
        implements=[
            Uri.from_str("ens/wraps.eth:http@1.1.0"),
            Uri.from_str("ens/wraps.eth:http@1.0.0"),
        ],
        redirects_from=[
            Uri.from_str("ens/wraps.eth:http@1.1.0"),
            Uri.from_str("ens/wraps.eth:http@1.0.0"),
        ],
    ),
    "http_resolver": BundlePackage(
        uri=Uri.from_str("embed/http-uri-resolver-ext@1.0.1"),
        package=get_embedded_wrap("http-resolver"),
        implements=[
            Uri.from_str("ens/wraps.eth:http-uri-resolver-ext@1.0.1"),
            *ExtendableUriResolver.DEFAULT_EXT_INTERFACE_URIS,
        ],
        redirects_from=[
            Uri.from_str("ens/wraps.eth:http-uri-resolver-ext@1.0.1"),
        ],
    ),
    "wrapscan_resolver": BundlePackage(
        uri=Uri.from_str(
            "wrap://https/wraps.wrapscan.io/r/polywrap/wrapscan-uri-resolver@1.0"
        ),
        implements=[
            Uri.from_str("wrapscan/polywrap/wrapscan-uri-resolver@1.0"),
            *ExtendableUriResolver.DEFAULT_EXT_INTERFACE_URIS,
        ],
        redirects_from=[Uri.from_str("wrapscan/polywrap/wrapscan-uri-resolver@1.0")],
    ),
    "github_resolver": BundlePackage(
        uri=Uri.from_str("wrap://ipfs/QmYPp2bQpRxR7WCoiAgWsWoiQzqxyFdqWxp1i65VW8wNv2"),
        implements=ExtendableUriResolver.DEFAULT_EXT_INTERFACE_URIS,
    ),
    "file_system": BundlePackage(
        uri=Uri.from_str("plugin/file-system@1.0.0"),
        package=file_system_plugin(),
        implements=[Uri.from_str("ens/wraps.eth:file-system@1.0.0")],
        redirects_from=[Uri.from_str("ens/wraps.eth:file-system@1.0.0")],
    ),
    "file_system_resolver": BundlePackage(
        uri=Uri.from_str("embed/file-system-uri-resolver-ext@1.0.1"),
        package=get_embedded_wrap("file-system-resolver"),
        implements=[
            Uri.from_str("ens/wraps.eth:file-system-uri-resolver-ext@1.0.1"),
            *ExtendableUriResolver.DEFAULT_EXT_INTERFACE_URIS,
        ],
        redirects_from=[
            Uri.from_str("ens/wraps.eth:file-system-uri-resolver-ext@1.0.1")
        ],
    ),
}


__all__ = ["sys_bundle"]
