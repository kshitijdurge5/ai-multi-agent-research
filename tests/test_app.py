from app import research_pipeline

def test_no_evidence_is_disclosed():
    r = research_pipeline('What happened?', '')
    assert 'No evidence' in r['report']
    assert 'verification' in r['steps'][-1]['output']
