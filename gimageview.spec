Summary:	Graphic Viewer
Summary(pl):	Przegl±darka plików graficznych
Name:		gimageview
Version:	0.2.25
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/sourceforge/gtkmmviewer/%{name}-%{version}.tar.gz
# Source0-md5:	82874cd6fecdc9833ce3f5745b4bd788
URL:		http://www.homa.ne.jp/~ashie/gimageview/
BuildRequires:	gtk+2-devel
BuildRequires:	imlib-devel
BuildRequires:	xcursor-devel
Requires:	glib >= 1.2.6
Requires:	gtk+2
Requires:	imlib >= 1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GImageView is a GTK+ based image viewer. It support tabbed browsing,
thumbnail table views, directory tree views, drag and drop, reading
thumbnail cache of other famous image viewers, and flexible user
interface.

%description -l pl
GImageView to bazujaca na GTK+ przegl±darka obrazków. Pozwala na
przegl±danie z zak³adkami, przegl±danie miniaturek i drzew katalogów,
obs³uguje drag-n-drop, potrafi odczytywaæ miniaturki z cache innych
przegl±darek obrazków i ma elastyczny interfejs u¿ytkownika.

%prep
%setup -q

%build

%configure \
	--with-gtk2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TIPS
%attr(755,root,root) %{_bindir}/gimv
%dir %{_datadir}/gimageview
%dir %{_datadir}/gimageview/pixmaps
%dir %{_datadir}/gimageview/pixmaps/default
%{_datadir}/gimageview/pixmaps/default/*.xpm
%dir %{_libdir}/gimageview
%dir %{_libdir}/gimageview/*
%attr(755,root,root) %{_libdir}/gimageview/*/*.so
