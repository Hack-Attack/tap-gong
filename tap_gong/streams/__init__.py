"""Stream type classes for tap-gong."""

from tap_gong.streams.aggregated_activity import AggregatedActivityStream
from tap_gong.streams.call_transcripts import CallTranscriptsStream
from tap_gong.streams.calls import CallsStream
from tap_gong.streams.interaction_stats import InteractionStatsStream
from tap_gong.streams.users import UsersStream

__all__ = [
    "CallsStream",
    "CallTranscriptsStream",
    "UsersStream",
    "InteractionStatsStream",
    "AggregatedActivityStream",
]
