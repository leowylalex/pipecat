#
# Copyright (c) 2024–2025, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

"""indue unified AI services for Pipecat.

This module provides unified access to various AI services through a single
managed API endpoint, abstracting away provider-specific implementations.

Named for indue, but the endpoint is Dograh's: these clients connect to
services.dograh.com, and every base_url default in this package is a Dograh
host. The class names say indue; the service answering does not. Those URLs
are correct as they stand -- don't "finish the rename" on them.
"""

from pipecat.services.indue.flux.stt import IndueFluxSTTService
from pipecat.services.indue.llm import IndueLLMService
from pipecat.services.indue.stt import IndueSTTService, IndueSTTSettings
from pipecat.services.indue.tts import IndueTTSService, IndueTTSSettings

__all__ = [
    "IndueFluxSTTService",
    "IndueLLMService",
    "IndueSTTService",
    "IndueSTTSettings",
    "IndueTTSService",
    "IndueTTSSettings",
]
