
import unittest
from django.test import TestCase
from unittest.mock import Mock, patch
from django.urls import reverse
from final_app.views import get_popular_podcasts, get_all_genres


class TestGetPopularPodcasts(unittest.TestCase):

    @patch('requests.get')
    def test_get_popular_podcasts_success(self, mock_get):
        # Symuluj odpowiedź z wywołania requests.get
        mock_response = Mock()
        mock_response.json.return_value = {
            "feed": {
                "entry": [
                    {
                        "id": {"label": "1"},
                        "im:artist": {"label": "Author 1"},
                        "im:name": {"label": "Podcast 1"},
                        "im:image": [{"label": "Logo URL 1"}],
                        "summary": {"label": "Summary 1"},
                        "category": {"attributes": {"label": "Category 1"}}
                    },
                    {
                        "id": {"label": "2"},
                        "im:artist": {"label": "Author 2"},
                        "im:name": {"label": "Podcast 2"},
                        "im:image": [{"label": "Logo URL 2"}],
                        "summary": {"label": "Summary 2"},
                        "category": {"attributes": {"label": "Category 2"}}
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        expected_result = [
            {
                "id": "1",
                "author": "Author 1",
                "name": "Podcast 1",
                "image": "Logo URL 1",
                "summary": "Summary 1.",
                "genre": "Category 1"
            },
            {
                "id": "2",
                "author": "Author 2",
                "name": "Podcast 2",
                "image": "Logo URL 2",
                "summary": "Summary 2.",
                "genre": "Category 2"
            }
        ]

        # Wywołaj funkcję, którą testujemy
        result = get_popular_podcasts()

        # Sprawdź, czy wynik jest zgodny z oczekiwanym rezultatem
        self.assertEqual(result, expected_result)


class TestGetAllGenres(unittest.TestCase):

    @patch('requests.get')
    def test_get_all_genres_success(self, mock_get):
        # Mockowanie odpowiedzi
        mock_response = {
            "feed": {
                "entry": [
                    {"category": {"attributes": {"label": "Category 1"}}},
                    {"category": {"attributes": {"label": "Category 2"}}},
                    {"category": {"attributes": {"label": "Category 1"}}}
                ]
            }
        }
        mock_get.return_value.json.return_value = mock_response

        # Oczekiwane gatunki
        expected_genres = ["Category 1", "Category 2"]

        # Wywołaj funkcję, którą testujemy
        result = get_all_genres()

        # Sprawdź, czy wynik jest taki sam, jak oczekiwane gatunki
        self.assertEqual(result, expected_genres)


class TestPost(TestCase):
    def test_invalid_genre_selected(self):
        # Przygotuj dane POST z nieprawidłowym gatunkiem
        data = {'genre': 'InvalidGenre'}
        url = reverse('form')

        # Wywołaj widok z danymi POST
        response = self.client.post(url, data)

        # Sprawdź, czy odpowiedź ma status 200
        self.assertEqual(response.status_code, 200)

        # Sprawdź, czy widok wyświetla odpowiedni komunikat
        self.assertContains(response, "Invalid genre name.")


