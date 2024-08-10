from unittest.mock import patch, call, Mock

from shared.requests_util import RequestsUtil


@patch("shared.requests_util.requests.Session")
def test_requests_util_get(m_req_session):
    m_req_session.return_value.get.return_value = Mock(json=lambda: {"some": "response"})
    req_util = RequestsUtil(bearer_token="some-token")
    resp = req_util.get(url="some-url", params={"param_one": "one", "param_two": "two"})
    assert resp == {'some': 'response'}
    assert m_req_session.mock_calls == [
        call(),
        call().headers.update({'content-type': 'application/json', 'Authorization': 'Bearer some-token'}),
        call().get(url='some-url', params={"param_one": "one", "param_two": "two"}),
        call().get().raise_for_status(),
    ]


@patch("shared.requests_util.requests.Session")
def test_requests_util_post(m_req_session):
    m_req_session.return_value.post.return_value = Mock(json=lambda: {"some": "response"})
    req_util = RequestsUtil(bearer_token="some-token")
    resp = req_util.post(url="some-url", body={"data": "value"})
    assert resp == {'some': 'response'}
    assert m_req_session.mock_calls == [
        call(),
        call().headers.update({'content-type': 'application/json', 'Authorization': 'Bearer some-token'}),
        call().post(url='some-url', data='{"data": "value"}'),
        call().post().raise_for_status(),
    ]
