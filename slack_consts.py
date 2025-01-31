# File: slack_consts.py
#
# Copyright (c) 2016-2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Action IDs
ACTION_ID_TEST_CONNECTIVITY = "test_connectivity"
ACTION_ID_LIST_CHANNELS = "list_channels"
ACTION_ID_POST_MESSAGE = "send_message"
ACTION_ID_ADD_REACTION = "add_reaction"
ACTION_ID_ASK_QUESTION = "ask_question"
ACTION_ID_GET_RESPONSE = "get_response"
ACTION_ID_UPLOAD_FILE = "upload_file"
ACTION_ID_LIST_USERS = "list_users"
ACTION_ID_GET_USER = "get_user"
ACTION_ID_STOP_BOT = "stop_bot"
ACTION_ID_ON_POLL = "on_poll"
ACTION_ID_CREATE_CHANNEL = "create_channel"
ACTION_ID_INVITE_USERS = "invite_users"

SLACK_BASE_URL = "https://slack.com/api/"
SLACK_MESSAGE_LIMIT = 4000
SLACK_DEFAULT_LIMIT = 100

SLACK_JSON_BOT_TOKEN = "bot_token"
SLACK_JSON_VERIFICATION_TOKEN = "verification_token"

SLACK_PHANTOM_ASSET_INFO_URL = "{url}rest/asset/{asset_id}"
SLACK_PHANTOM_SYS_INFO_URL = "{url}rest/system_info"
SLACK_PHANTOM_ICON = "https://www.phantom.us/img/phantom_icon_160x160.png"

SLACK_APP_ID = "3ac26c7f-baa4-4583-86ff-5aac82778a86"

SLACK_ADD_REACTION = "reactions.add"
SLACK_CHANNEL_CREATE_ENDPOINT = "conversations.create"
SLACK_INVITE_TO_CHANNEL = "conversations.invite"
SLACK_LIST_CHANNEL = "conversations.list"
SLACK_AUTH_TEST = "auth.test"
SLACK_USER_LIST = "users.list"
SLACK_USER_INFO = "users.info"
SLACK_SEND_MESSAGE = "chat.postMessage"
SLACK_UPLOAD_FILE = "files.upload"

SLACK_TC_STATUS_SLEEP = 2
SLACK_TC_FILE = "slack_auth_task.out"

SLACK_SUCC_MESSAGE = "Slack message post successful"

SLACK_ERR_MESSAGE_RETURNED_NO_DATA = "Message post did not receive response"
SLACK_ERR_SERVER_CONNECTION = "Connection to server failed"
SLACK_ERR_UNSUPPORTED_METHOD = "Unsupported method"
SLACK_ERR_FROM_SERVER = "Got unknown error from the Slack server"
SLACK_ERR_NOT_IN_VAULT = "No item in vault has the supplied ID"
SLACK_ERR_CODE_UNAVAILABLE = "Error code unavailable"
SLACK_ERR_MESSAGE_UNKNOWN = "Unknown error occurred. Please check the asset configuration and|or action parameters"
SLACK_UNICODE_DAMMIT_TYPE_ERR_MESSAGE = ("Error occurred while connecting to the Slack server. "
"Please check the asset configuration and|or the action parameters")
SLACK_ERR_INVALID_FILE_PATH = "The file path is invalid"
SLACK_ERR_INVALID_INT = "Please provide a valid integer value in the {key} parameter"
SLACK_ERR_NEGATIVE_AND_ZERO_INT = "Please provide a valid non-zero positive integer value in the {key} parameter"
SLACK_ERR_NEGATIVE_INT = "Please provide a valid non-negative integer value in the {key} parameter"
SLACK_ERR_UNABLE_TO_FETCH_FILE = "Unable to fetch the file {key}"
SLACK_ERR_PAYLOAD_NOT_FOUND = "Found no payload field in rest post body"
SLACK_ERR_CALLBACK_ID_NOT_FOUND = "Found no callback_id field in payload"
SLACK_ERR_PARSE_JSON_FROM_CALLBACK_ID = "Could not parse JSON from callback_id field in payload: {error}"
SLACK_ERR_STATE_DIR_NOT_FOUND = "Found no state directory in callback"
SLACK_ERR_UNEXPECTED_STATE_DIR = "Unexpected state directory found in callback"
SLACK_ERR_STATE_FILE_NOT_FOUND = "Found no state filename in callback"
SLACK_ERR_UNABLE_TO_READ_STATE_FILE = "Could not properly read state file: {error}"
SLACK_ERR_AUTH_FAILED = "Authorization failed. Tokens do not match."
SLACK_ERR_ANSWER_FILE_NOT_FOUND = "Found no answer filename in callback"
SLACK_ERR_COULD_NOT_OPEN_ANSWER_FILE = "Could not open answer file for writing: {error}"
SLACK_ERR_WHILE_WRITING_ANSWER_FILE = "Error occurred while writing in answer file: {error}"
SLACK_ERR_PROCESS_RESPONSE = "There was an error processing the response: {error}"
SLACK_ERR_FETCHING_PYTHON_VERSION = "Error occurred while fetching the Phantom server's Python major version"
SLACK_ERR_PY_2TO3 = "Error occurred while handling python 2to3 compatibility for the input string"
SLACK_ERR_BASE_URL_NOT_FOUND = "Phantom Base URL not found in System Setting. Please specify this value in System Settings"
SLACK_ERR_EMPTY_RESPONSE = "Status Code {code}. Empty response and no information in the header"
SLACK_UNABLE_TO_PARSE_ERR_DETAILS = "Cannot parse error details"
SLACK_ERR_UNABLE_TO_PARSE_JSON_RESPONSE = "Unable to parse response as JSON. {error}"
SLACK_ERR_BOT_TOKEN_INVALID = "The configured bot token is invalid"
SLACK_ERR_NOT_IN_CHANNEL = "The configured bot is not in the specified channel. Invite the bot to that channel to send messages there."
SLACK_ERR_UNABLE_TO_DECODE_JSON_RESPONSE = "Unable to decode the response as JSON"
SLACK_ERR_REST_CALL_FAILED = "REST call failed"
SLACK_ERR_TEST_CONN_FAILED = "Test Connectivity Failed"
SLACK_SUCC_TEST_CONN_PASSED = "Test Connectivity Passed"
SLACK_ERR_USER_TOKEN_NOT_PROVIDED = ("'OAuth Access Token' is required for this action. "
"Navigate to the asset's configuration and add a token now and try again.")
SLACK_ERR_CREATING_CHANNEL = "Error creating channel"
SLACK_SUCC_CHANNEL_CREATED = "Channel created successfully"
SLACK_ERR_DATA_NOT_FOUND_IN_OUTPUT = "{key} data not found in json output"
SLACK_ERR_NOT_A_USER_ID = "The user parameter must be a user ID"
SLACK_SUCC_USER_DATA_RETRIEVED = "User data successfully retrieved"
SLACK_ERR_INVALID_USER = "Please provide a valid value in 'users' action parameter"
SLACK_ERR_INVITING_CHANNEL = "Error inviting to channel"
SLACK_ERR_ADDING_REACTION = "Error adding reaction"
SLACK_ERR_ASKING_QUESTION = "Error asking question"
SLACK_ERR_SENDING_MESSAGE = "Error sending message"
SLACK_ERR_UPLOADING_FILE = "Error uploading file"
SLACK_ERR_FETCHING_USER = "Error fetching user"
SLACK_SUCC_INVITE_SENT = "Invite sent to user(s)"
SLACK_ERR_MESSAGE_TOO_LONG = "Message too long. Please limit messages to {limit} characters."
SLACK_ERR_QUESTION_TOO_LONG = "Question too long. Please limit questions to {limit} characters."
SLACK_SUCC_MESSAGE_SENT = "Message sent successfully"
SLACK_SUCC_REACTION_ADDED = "Reaction added successfully"
SLACK_ERR_FILE_OR_CONTENT_NOT_PROVIDED = "Please provide either a 'file' or 'content' to upload"
SLACK_SUCC_FILE_UPLOAD = "File uploaded successfully"
SLACK_SUCC_SLACKBOT_STOPPED = "SlackBot has been stopped."
SLACK_SUCC_SLACKBOT_NOT_RUNNING = "SlackBot isn't running, not going to stop it."
SLACK_FAILED_TO_DISABLE_INGESTION = "{message} Failed to disable ingestion, please check that ingest settings are correct."
SLACK_INGESTION_NOT_ENABLED = "{message} Ingestion isn't enabled, not going to disable it."
SLACK_INGESTION_DISABLED = "{message} Ingestion has been disabled."
SLACK_ERR_COULD_NOT_GET_BOT_ID = "Could not get bot ID from Slack"
SLACK_SUCC_SLACKBOT_RUNNING = "SlackBot already running"
SLACK_ERR_AUTH_TOKEN_NOT_PROVIDED = "The 'ph_auth_token' asset configuration parameter is required to run the on_poll action"
SLACK_ERR_SLACKBOT_RUNNING_WITH_SAME_BOT_TOKEN = ("Detected an instance of SlackBot running with the same bot token. "
"Not going to start new instance.")
SLACK_SUCC_SLACKBOT_STARTED = "SlackBot started"
SLACK_ERR_UNABLE_TO_SEND_QUESTION_TO_CHANNEL = "Questions may only be sent as direct messages to users. They may not be sent to channels."
SLACK_ERR_UNABLE_TO_PARSE_RESPONSE = "Error occurred while parsing the response"
SLACK_ERR_QUESTION_RESPONSE_NOT_AVAILABLE = "Response to question not available"
SLACK_ERR_NO_RESPONSE_FROM_SERVER = "Got no response from the Slack server"
SLACK_ERR_INVALID_CHANNEL_TYPE = "Please provide a valid value in the 'channel_type' action parameter"
SLACK_ERR_LENGTH_LIMIT_EXCEEDED = ("Based on your asset_id length ({asset_length}), "
"valid length for the 'confirmation' parameter is {valid_length}")

SLACK_RESP_POLL_INTERVAL_KEY = "'How often to poll for a response (in seconds)' configuration"
SLACK_TIMEOUT_KEY = "'Question timeout (in minutes)' configuration"
SLACK_TOTAL_RESP_KEY = "'Total number of responses to keep' configuration"
SLACK_LIMIT_KEY = "'limit' action"

SLACK_DEFAULT_TIMEOUT = 30
