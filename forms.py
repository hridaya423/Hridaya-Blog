from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, URL
from wtforms_components import ColorField


class CreatePostForm(FlaskForm):
    title = StringField("Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    navigation_bar_color = ColorField()
    img_url = StringField("Post Image URL")
    body = CKEditorField("Post Content", validators=[DataRequired()])
    submit = SubmitField("Submit", render_kw={"style": "margin-top: 20px;"})


class ForgetPasswordForm(FlaskForm):
    new_password = PasswordField("Enter your new password:", validators=[DataRequired()])
    submit = SubmitField("Submit", render_kw={"style": "margin-top: 20px;"})


class ForgetHandlingForm(FlaskForm):
    email = StringField("Enter your email address:", validators=[DataRequired(), Email()])
    submit = SubmitField("Proceed", render_kw={"style": "margin-top: 20px;"})


class WebConfigForm(FlaskForm):
    name = StringField("Website Name", validators=[DataRequired()],
                       render_kw={"style": "margin-bottom: 10px;"})
    homepage_title = StringField("Homepage Title", validators=[DataRequired()],
                                 render_kw={"style": "margin-bottom: 10px;"})
    homepage_subtitle = StringField("Homepage Subtitle", validators=[DataRequired()],
                                    render_kw={"style": "margin-bottom: 10px;"})
    navigation_bar_color = ColorField()
    background_image = StringField("Background Image URL",
                                   render_kw={"style": "margin-bottom: 10px;"})
    twitter_link = StringField("Twitter Link",
                               render_kw={"style": "margin-bottom: 10px;"})
    facebook_link = StringField("FaceBook Link",
                                render_kw={"style": "margin-bottom: 10px;"})
    github_link = StringField("GitHub Link",
                              render_kw={"style": "margin-bottom: 10px;"})
    youtube_link = StringField("YouTube Link",
                               render_kw={"style": "margin-bottom: 10px;"})
    linkedin_link = StringField("LinkedIn Link",
                                render_kw={"style": "margin-bottom: 10px;"})
    instagram_link = StringField("Instagram Link",
                                 render_kw={"style": "margin-bottom: 10px;"})
    dev_link = StringField("Dev Link",
                           render_kw={"style": "margin-bottom: 10px;"})
    submit = SubmitField("Save Changes", render_kw={"style": "margin-top: 20px;"})


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign up", render_kw={"style": "margin-top: 20px;"})


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in", render_kw={"style": "margin-top: 25px;"})


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = CKEditorField("Your Message", validators=[DataRequired()])
    submit = SubmitField("Send Message", render_kw={"style": "margin-top: 20px;"})


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment", render_kw={"style": "margin-top: 20px;"})


class EditCommentForm(FlaskForm):
    comment = CKEditorField("Edit Comment", validators=[DataRequired()])
    submit = SubmitField("Save Changes", render_kw={"style": "margin-top: 20px;"})


class EditReplyForm(FlaskForm):
    reply = CKEditorField("Edit Reply", validators=[DataRequired()])
    submit = SubmitField("Save Changes", render_kw={"style": "margin-top: 20px;"})


class ReplyForm(FlaskForm):
    reply = CKEditorField("Reply", validators=[DataRequired()])
    submit = SubmitField("Submit Reply", render_kw={"style": "margin-top: 20px;"})


class SearchForm(FlaskForm):
    category = SelectField("Category", choices=[('posts', 'Posts'), ('users', 'Users')])
    search = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search", render_kw={"style": "margin-top: 20px;"})


class DeleteForm(FlaskForm):
    title = StringField("Action Title", validators=[DataRequired()])
    reason = CKEditorField("Action Reason", validators=[DataRequired()])
    submit = SubmitField("Delete Account", render_kw={"style": "margin-top: 20px;"})


class AuthForm(FlaskForm):
    code = PasswordField("Authorization Code", validators=[DataRequired()])
    submit = SubmitField("Authenticate", render_kw={"style": "margin-top: 20px;"})


class ContactConfigForm(FlaskForm):
    page_heading = StringField("Contact Page Title", validators=[DataRequired()])
    page_subheading = StringField("Contact Page Subtitle", validators=[DataRequired()])
    page_description = StringField("Contact Page Description", validators=[DataRequired()])
    background_image = StringField("Contact Page Background Image", validators=[URL()])
    support_email = StringField("Contact Support Email (Inquires will be directed to the specified email)",
                                validators=[DataRequired(), Email()])
    submit = SubmitField("Save changes", render_kw={"style": "margin-top: 20px;"})


class AboutConfigForm(FlaskForm):
    page_heading = StringField("About Page Title", validators=[DataRequired()])
    page_subheading = StringField("About Page Subtitle", validators=[DataRequired()])
    background_image = StringField("About Page Background Image", validators=[URL()])
    page_content = CKEditorField("About Page Content", validators=[DataRequired()])
    submit = SubmitField("Save changes", render_kw={"style": "margin-top: 20px;"})


class MakeUserForm(FlaskForm):
    reason = CKEditorField("Reason for Action", validators=[DataRequired()])
    submit = SubmitField("Proceed", render_kw={"style": "margin-top: 20px;"})


class AuthConfig(FlaskForm):
    old_password = PasswordField("Old Authentication Password", validators=[DataRequired()])
    new_password = PasswordField("New Authentication Password", validators=[DataRequired()])
    submit = SubmitField("Change Authentication Password", render_kw={"style": "margin-top: 20px;"})


class ApiConfig(FlaskForm):
    all_posts = BooleanField("All Posts Route")
    all_users = BooleanField("Users Route")
    random_post = BooleanField("Random Post Route")
    submit = SubmitField("Save Changes", render_kw={"style": "margin-top: 20px;"})


class ApiGenerate(FlaskForm):
    occupation = SelectField("What are you?", choices=[('Student', 'Student'), ('Professional Developer',
                                                                                'Professional Developer'),
                                                       ('Hobbyist', 'Hobbyist'), ('Other', 'Other')])
    application = StringField("Tell us about your application in short.", validators=[DataRequired()])
    usage = CKEditorField("What will you be using our API service for?", validators=[DataRequired()])
    submit = SubmitField("Generate API Key", render_kw={"style": "margin-top: 20px;"})


class DeletionRequest(FlaskForm):
    reason = SelectField("Why are you deleting your account?", choices=[('Dissatisfied', 'Dissatisfied'),
                                                                        ('Not Interested', 'Not Interested'),
                                                                        ("Bad User Experience", "Bad User Experience"),
                                                                        ('Other', 'Other')])
    explanation = CKEditorField("Could you tell us more?")
    submit = SubmitField("Delete my account", render_kw={"style": "margin-top: 20px;"})