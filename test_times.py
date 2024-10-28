from times import time_range
from times import compute_overlap_time

def test_compute_overlap_time():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00")
    
    expected = [("2010-01-12 13:30:00", "2010-01-12 12:00:00")]
    assert compute_overlap_time(large, short) == expected